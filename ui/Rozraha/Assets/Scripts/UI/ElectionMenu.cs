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
		private GameObject submitLocker;

		private List<CandidatePanel> spawnedCandidates = new List<CandidatePanel>();

		private Election currentElection;

		private void Awake()
		{
			this.submitButton.onClick.AddListener(this.OnSubmitted);
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
		}

		public void SetUp(Election election)
		{
			this.electionIdLabel.text = $"Election {election.pk}";
			this.availableVotesLabel.text = $"Votes left: {election.type.votesCount}";
			this.currentElection = election;
			this.currentElection.CheckVotedStatus();

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
			TimeSpan remainingTime = this.currentElection.end - DateTime.UtcNow;
			this.remainingTimeLabel.text = $"Remaining time: {remainingTime.Days} days," +
				$" {remainingTime.Hours} hours," +
				$" {remainingTime.Seconds} seconds";
		}

		private void OnSubmitted()
		{
			PlayerPrefs.SetString(this.currentElection.pk.ToString(), "1");
			if (!this.currentElection.type.cancelable)
			{
				this.Lock();
			}
		}

		private void OnVoted(int votesCount)
		{
			this.availableVotesLabel.text = $"Votes left: {votesCount}";
		}

		private void CreateCandidate(User candidateUser)
		{
			CandidatePanel candidate = Instantiate(this.candidatePanel, this.candidatesContainer);
			candidate.SetUp(candidateUser, this.currentElection.type);
			candidate.Voted += this.OnVoted;
			this.spawnedCandidates.Add(candidate);
		}

		private void UnsubscribeCandidates()
		{
			foreach (CandidatePanel candidate in this.spawnedCandidates)
			{
				candidate.Voted -= this.OnVoted;
			}
		}

		private void ClearCandidates()
		{
			this.UnsubscribeCandidates();
			for (int i = 0; i < this.candidatesContainer.childCount; i++)
			{
				Destroy(this.candidatesContainer.GetChild(i));
			}
			this.spawnedCandidates.Clear();
		}
	}
}
