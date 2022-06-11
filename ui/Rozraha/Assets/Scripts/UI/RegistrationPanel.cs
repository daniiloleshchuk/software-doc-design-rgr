using Rozraha.Backend.Controllers;
using Rozraha.Backend.Models;
using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace Rozraha.UI
{
	public class RegistrationPanel : MonoBehaviour
    {
		[SerializeField]
		private TMP_Dropdown regionsDropdown;

		[SerializeField]
		private TMP_InputField nameInput;

		[SerializeField]
		private TMP_InputField ageInput;

		[SerializeField]
		private TMP_InputField passportId;

		[SerializeField]
		private Toggle organizationMember;

		[SerializeField]
		private Button submitButton;

		private List<Region> regionOptions = new List<Region>();

        private RegionController regionController = new RegionController();

		private UserController userController = new UserController();

		private RegistrationPrefsHandler registrationPrefsHandler = new RegistrationPrefsHandler();

		private int selectedRegionIndex;

		private void Awake()
		{
			int registered = this.registrationPrefsHandler.LoadFromPrefs();
			if (registered == 0)
			{
				Region region = new Region { name = "Pavlo" };
				Region region1 = new Region { name = "Vlad" };
				Region region2 = new Region { name = "Amogus" };

				this.regionOptions.Add(region);
				this.regionOptions.Add(region1);
				this.regionOptions.Add(region2);

				this.regionsDropdown.AddOptions(this.regionOptions.Select(x => x.name).ToList());

				this.regionsDropdown.onValueChanged.AddListener((index) => this.OnDropdownSelected(index));

				this.submitButton.onClick.AddListener(this.OnSubmitButtonClicked);
			}
		}

		private void OnDestroy()
		{
			this.regionsDropdown.onValueChanged.RemoveAllListeners();
			this.submitButton.onClick.RemoveAllListeners();
		}

		private async void InitializeRegions()
		{
			/* Supposed to work with non hardcoded values
			this.regionOptions = await this.regionController.GetAllEntities();

			this.regionsDropdown.AddOptions(this.regionOptions.Select(x => x.name).ToList());
			*/
		}

		private void OnDropdownSelected(int index)
		{
			this.selectedRegionIndex = index;
			Debug.Log("Dropdown selected");
		}

		private void OnSubmitButtonClicked()
		{
			/* Supposed to work with non hardcoded values
			User newUser = this.ConstructUser();
			this.userController.CreateEntity(newUser);
			this.registrationPrefsHandler.SaveToPrefs(1);
			*/
			Debug.Log("Submitted");
		}

		private User ConstructUser()
		{
			User user = new User();
			user.age = int.Parse(this.ageInput.text);
			user.isOrganizationMember = this.organizationMember.isOn;
			user.name = this.nameInput.text;
			user.passportId = this.passportId.text;
			user.regionPk = this.selectedRegionIndex;
			return user;
		}
	}
}
