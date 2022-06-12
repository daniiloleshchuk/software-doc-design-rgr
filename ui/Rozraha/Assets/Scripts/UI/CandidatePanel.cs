using Rozraha.Backend.Models;
using System;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace Rozraha.UI
{
	public class CandidatePanel : MonoBehaviour
	{
		public event Action<int> Voted;

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

		private void Awake()
		{
			this.addVoteButton.onClick.AddListener(this.AddVote);
			this.removeVoteButton.onClick.AddListener(this.RemoveVote);
		}

		private void Update()
		{
			this.addVoteButton.interactable = this.VotesCount > 0;
		}

		private void OnDestroy()
		{
			this.addVoteButton.onClick.RemoveAllListeners();
			this.removeVoteButton.onClick.RemoveAllListeners();
		}

		public void SetUp(User candidate, ElectionType electionType)
		{
			this.nameLabel.text = candidate.name;
			this.ageLabel.text = candidate.age.ToString();
			this.votesCountLabel.text = electionType.votesCount.ToString();
			this.VotesCount = electionType.votesCount;
			this.Candidate = candidate;
		}

		public void Lock()
		{
			this.addVoteButton.interactable = false;
			this.removeVoteButton.interactable = false;
		}

		private void AddVote()
		{
			this.VotesCount--;
			this.Voted?.Invoke(this.VotesCount);
		}

		private void RemoveVote()
		{
			this.VotesCount++;
			this.Voted?.Invoke(this.VotesCount);
		}
	}
}
