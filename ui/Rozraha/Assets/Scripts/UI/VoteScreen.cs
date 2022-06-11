using Rozraha.Backend.Controllers;
using Rozraha.Backend.Models;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Rozraha.UI
{
	public class VoteScreen : MonoBehaviour
	{
		private List<Election> elections;

		private ElectionController electionController = new ElectionController();

		private void Awake()
		{
			this.InitializeElections();
		}

		private async void InitializeElections()
		{
			this.elections = await this.electionController.GetAllEntities();
		}
	}
}
