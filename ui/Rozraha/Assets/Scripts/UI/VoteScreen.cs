using Rozraha.Backend.Controllers;
using Rozraha.Backend.Models;
using Rozraha.Events;
using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using TMPro;

namespace Rozraha.UI
{
	public class VoteScreen : MonoBehaviour
	{
		[SerializeField]
		private ElectionButton electionButton;

		[SerializeField]
		private ElectionMenu electionMenu;

		[SerializeField]
		private Transform electionButtonsContainer;

		private List<Election> elections;

		public User CurrentUser { get; private set; }

		private ElectionController electionController = new ElectionController();

		private void Awake()
		{
			EventAggregator.Instance.Subscribe<UserCreated>(this.OnUserCreated);
		}

		private void OnEnable()
		{
			this.InitializeElections();
		}

		private void OnDestroy()
		{
			EventAggregator.Instance.Unsubscribe<UserCreated>(this.OnUserCreated);
		}

		private async void InitializeElections()
		{
			this.elections = await this.electionController.GetAllEntities();
			Election election = this.elections.Find(x => !this.UserUnableToVote(x));
			if (election != null)
			{
				this.electionMenu.SetUp(election);
			}
			this.PopulateElectionButtons();
		}

		private void PopulateElectionButtons()
		{
			foreach (Election election in this.elections)
			{
				ElectionButton spawnedButton = Instantiate(this.electionButton, this.electionButtonsContainer);
				spawnedButton.SetUp(election, this.electionMenu);
				if (this.UserUnableToVote(election))
				{
					spawnedButton.Lock();
				}
			}
		}

		private bool UserUnableToVote(Election election)
		{
			ElectionType electionType = election.type;
			return this.CurrentUser.isOrganizationMember != electionType.organizationMembersOnly
				|| !electionType.regionsAllowed.Any(x => x.pk == this.CurrentUser.regionPk)
				|| !this.ValidateUserAge(this.CurrentUser, electionType)
				|| !(DateTime.Now > election.start)
				|| !(DateTime.Now < election.end);
		}

		private bool ValidateUserAge(User user, ElectionType electionType)
		{
			bool isValidAge = true;
			if (electionType.ageFrom != null)
			{
				isValidAge = user.age > electionType.ageFrom;
			}
			if (electionType.ageTo != null && isValidAge)
			{
				isValidAge = user.age < electionType.ageTo;
			}
			return isValidAge;
		}

		private void OnUserCreated(UserCreated args)
		{
			this.CurrentUser = args.user;
		}
	}
}
