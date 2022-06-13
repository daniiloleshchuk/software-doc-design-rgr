using UnityEngine;
using TMPro;

namespace Rozraha.UI
{
	public class CandidateStatsView : MonoBehaviour
	{
		[SerializeField]
		private TextMeshProUGUI nameLabel;

		[SerializeField]
		private TextMeshProUGUI regionLabel;

		[SerializeField]
		private TextMeshProUGUI votesCount;

		public void SetUp(CandidateInfo candidateInfo)
		{
			this.nameLabel.text = $"Name: {candidateInfo.name}";
			this.regionLabel.text = $"Region: {candidateInfo.region}";
			this.votesCount.text = $"Votes: {candidateInfo.votesCount}";
		}
	}
}
