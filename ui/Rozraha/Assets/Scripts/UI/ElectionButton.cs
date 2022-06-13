using Rozraha.Backend.Models;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

namespace Rozraha.UI
{
	[RequireComponent(typeof(Button))]
	public class ElectionButton : MonoBehaviour
	{
		[SerializeField]
		private TextMeshProUGUI label;

		[SerializeField]
		private Image locker;

		private ElectionMenu electionMenu;

		private Button buttonComponent;

		private Election linkedElection;

		private void Awake()
		{
			this.buttonComponent = this.GetComponent<Button>();
			this.buttonComponent.onClick.AddListener(this.OnElectionSelected);
		}

		private void OnDestroy()
		{
			this.buttonComponent.onClick.RemoveAllListeners();
		}

		public void SetUp(Election election, ElectionMenu electionMenu)
		{
			this.label.text = $"Election {election.pk}";
			this.electionMenu = electionMenu;
			this.linkedElection = election;
		}

		public void Lock()
		{
			this.locker.gameObject.SetActive(true);
			this.label.gameObject.SetActive(false);
			this.buttonComponent.interactable = false;
		}

		private void OnElectionSelected()
		{
			this.electionMenu.SetUp(this.linkedElection);
		}
	}
}
