using Rozraha.Backend.Controllers;
using Rozraha.Backend.Models;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace Rozraha.UI
{
	public class StatsPanel : MonoBehaviour
	{
		[SerializeField]
		private CandidateStatsView candidateStatsView;

		[SerializeField]
		private Transform candidateStatsContainer;

		[SerializeField]
		private RegistrationPanel registrationPanel;

		[SerializeField]
		private Button closeButton;

		private CandidateWithStatsController candidateWithStatsController = new CandidateWithStatsController();

		private void Awake()
		{
			this.closeButton.onClick.AddListener(this.OnClosed);
		}

		private void OnDestroy()
		{
			this.closeButton.onClick.RemoveAllListeners();
		}

		public void SetUp(int electionId)
		{
			this.SetUpStatsAsync(electionId);
		}

		private async void SetUpStatsAsync(int electionId)
		{
			this.ClearCandidates();

			List<CandidateWithStats> candidates = await this.candidateWithStatsController.GetAllEntitiesById(electionId);

			candidates.Sort((p, q) => q.totalVotes.CompareTo(p.totalVotes));

			foreach (CandidateWithStats candidate in candidates)
			{
				this.ConstructCandidate(candidate);
			}
			this.gameObject.SetActive(true);
		}

		private void ConstructCandidate(CandidateWithStats candidateWithStats)
		{
			Region region = this.registrationPanel.regionOptions.Find(x => x.pk == candidateWithStats.candidate.regionPk);

			CandidateStatsView candidateStatsView = Instantiate(this.candidateStatsView, this.candidateStatsContainer);
			candidateStatsView.SetUp(new CandidateInfo(candidateWithStats.candidate.name, region.name, candidateWithStats.totalVotes));
		}

		private void OnClosed()
		{
			this.ClearCandidates();
			this.gameObject.SetActive(false);
		}

		private void ClearCandidates()
		{
			for (int i = 0; i < this.candidateStatsContainer.childCount; i++)
			{
				Destroy(this.candidateStatsContainer.GetChild(i).gameObject);
			}
		}
	}
}
