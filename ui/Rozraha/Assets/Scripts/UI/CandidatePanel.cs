using Rozraha.Backend.Models;
using System;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace Rozraha.UI
{
	public class CandidatePanel : MonoBehaviour
	{
		public event Action VoteAdded;
		public event Action VoteRemoved;

		[SerializeField]
		private TextMeshProUGUI nameLabel;

		[SerializeField]
		private TextMeshProUGUI ageLabel;

		[SerializeField]
		private TextMeshProUGUI votesCountLabel;

		[SerializeField]
		private Button addVoteButton;

		[SerializeField]
		private Button removeVoteButton;

		public int VotesCount { get; private set; }

		public User Candidate { get; private set; }

		private ElectionMenu electionMenu;

		private void Awake()
		{
			this.addVoteButton.onClick.AddListener(this.AddVote);
			this.removeVoteButton.onClick.AddListener(this.RemoveVote);
		}

		private void Update()
		{
			this.addVoteButton.interactable = this.electionMenu.VotesCount > 0;
			this.removeVoteButton.interactable = this.VotesCount > 0;
		}

		private void OnDestroy()
		{
			this.addVoteButton.onClick.RemoveAllListeners();
			this.removeVoteButton.onClick.RemoveAllListeners();
		}

		public void SetUp(User candidate, ElectionType electionType, ElectionMenu electionMenu)
		{
			this.nameLabel.text = candidate.name;
			this.ageLabel.text = candidate.age.ToString();
			this.Candidate = candidate;
			this.electionMenu = electionMenu;
		}

		public void Lock()
		{
			this.addVoteButton.interactable = false;
			this.removeVoteButton.interactable = false;
		}

		private void AddVote()
		{
			if (this.electionMenu.VotesCount > 0)
			{
				this.VotesCount++;
				this.votesCountLabel.text = this.VotesCount.ToString();
				this.VoteAdded?.Invoke();
			}
		}

		private void RemoveVote()
		{
			if (this.VotesCount > 0)
			{
				this.VotesCount--;
				this.votesCountLabel.text = this.VotesCount.ToString();
				this.VoteRemoved?.Invoke();
			}
		}
	}
}
