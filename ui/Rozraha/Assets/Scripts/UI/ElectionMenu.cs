using Rozraha.Backend.Controllers;
using Rozraha.Backend.Models;
using System;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace Rozraha.UI
{
	public class ElectionMenu : MonoBehaviour
	{
		[SerializeField]
		private TextMeshProUGUI electionIdLabel;

		[SerializeField]
		private TextMeshProUGUI remainingTimeLabel;

		[SerializeField]
		private TextMeshProUGUI availableVotesLabel;

		[SerializeField]
		private Transform candidatesContainer;

		[SerializeField]
		private CandidatePanel candidatePanel;

		[SerializeField]
		private Button submitButton;

		[SerializeField]
		private Button statsButton;

		[SerializeField]
		private GameObject submitLocker;

		[SerializeField]
		private VoteScreen voteScreen;

		[SerializeField]
		private StatsPanel statsPanel;

		private List<CandidatePanel> spawnedCandidates = new List<CandidatePanel>();

		private Election currentElection;

		private VoteController voteController = new VoteController();

		public int VotesCount { get; private set; }

		private void Awake()
		{
			this.submitButton.onClick.AddListener(this.OnSubmitted);
			this.statsButton.onClick.AddListener(this.OnStatsOpened);
		}

		private void Update()
		{
			if (this.currentElection != null)
			{
				this.UpdateRemainingTime();
			}
		}

		private void OnDestroy()
		{
			this.submitButton.onClick.RemoveAllListeners();
			this.statsButton.onClick.RemoveAllListeners();
		}

		public void SetUp(Election election)
		{
			this.electionIdLabel.text = $"Election {election.pk}";
			this.currentElection = election;
			this.currentElection.CheckVotedStatus();
			this.VotesCount = election.type.votesCount;
			this.availableVotesLabel.text = $"Votes left: {this.VotesCount}";

			if (this.statsPanel.gameObject.activeSelf)
			{
				this.OnStatsOpened();
			}

			if (this.currentElection.voted && !election.type.cancelable)
			{
				this.Lock();
				return;
			}

			if (this.spawnedCandidates.Count > 0)
			{
				this.ClearCandidates();
			}

			foreach (User candidateUser in this.currentElection.candidates)
			{
				this.CreateCandidate(candidateUser);
			}
		}

		public void Lock()
		{
			foreach (CandidatePanel candidate in this.spawnedCandidates)
			{
				candidate.Lock();
			}
			this.submitLocker.SetActive(false);
		}

		private void UpdateRemainingTime()
		{
			TimeSpan remainingTime = this.currentElection.end - DateTime.Now;
			this.remainingTimeLabel.text = $"Remaining time: {remainingTime.Days}d," +
				$" {remainingTime.Hours}h," +
				$" {remainingTime.Minutes}m";
		}

		private void OnStatsOpened()
		{
			this.statsPanel.SetUp(this.currentElection.pk);
		}

		private void OnSubmitted()
		{
			PlayerPrefs.SetString(this.currentElection.pk.ToString(), "1");
			if (!this.currentElection.type.cancelable)
			{
				this.Lock();
			}

			Vote vote = new Vote();
			vote.electionId = this.currentElection.pk;
			vote.electionPk = this.currentElection.pk;
			vote.voterId = this.voteScreen.CurrentUser.pk;
			vote.regionId = this.voteScreen.CurrentUser.regionPk;
			vote.votingData = new Dictionary<int, int>();

			foreach(CandidatePanel candidate in this.spawnedCandidates)
			{
				if (candidate.VotesCount > 0)
				{
					vote.votingData.Add(candidate.Candidate.pk, candidate.VotesCount);
				}
			}

			this.voteController.CreateEntity(vote);
		}

		private void VoteAdded()
		{
			this.VotesCount--;
			this.availableVotesLabel.text = $"Votes left: {this.VotesCount}";
		}

		private void VoteRemoved()
		{
			this.VotesCount++;
			this.availableVotesLabel.text = $"Votes left: {this.VotesCount}";
		}

		private void CreateCandidate(User candidateUser)
		{
			CandidatePanel candidate = Instantiate(this.candidatePanel, this.candidatesContainer);
			candidate.SetUp(candidateUser, this.currentElection.type, this);
			candidate.VoteAdded += this.VoteAdded;
			candidate.VoteRemoved += this.VoteRemoved;
			this.spawnedCandidates.Add(candidate);
		}

		private void UnsubscribeCandidates()
		{
			foreach (CandidatePanel candidate in this.spawnedCandidates)
			{
				candidate.VoteAdded -= this.VoteAdded;
				candidate.VoteRemoved -= this.VoteRemoved;
			}
		}

		private void ClearCandidates()
		{
			this.UnsubscribeCandidates();
			for (int i = 0; i < this.candidatesContainer.childCount; i++)
			{
				Destroy(this.candidatesContainer.GetChild(i).gameObject);
			}
			this.spawnedCandidates.Clear();
		}
	}
}
