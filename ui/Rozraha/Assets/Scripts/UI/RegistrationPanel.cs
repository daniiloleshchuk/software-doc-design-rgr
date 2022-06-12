using Rozraha.Backend.Controllers;
using Rozraha.Backend.Models;
using Rozraha.Events;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
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

		[SerializeField]
		private GameObject voteScreen;

		[SerializeField]
		private GameObject errorMessage;

		private List<Region> regionOptions = new List<Region>();

		private RegionController regionController = new RegionController();

		private UserController userController = new UserController();

		private RegistrationPrefsHandler registrationPrefsHandler = new RegistrationPrefsHandler();

		private int selectedRegionIndex;

		private User currentUser;

		private void Awake()
		{
			int storedId = this.registrationPrefsHandler.LoadFromPrefs	();

			if (storedId > 0)
			{
				_ = this.OnUserStoredAsync(storedId);
			}

			this.InitializeRegions();

			this.regionsDropdown.onValueChanged.AddListener((index) => this.OnDropdownSelected(index));

			this.submitButton.onClick.AddListener(this.OnSubmitButtonClickedAsync);
		}

		private void OnDestroy()
		{
			this.regionsDropdown.onValueChanged.RemoveAllListeners();
			this.submitButton.onClick.RemoveAllListeners();
		}

		private async void InitializeRegions()
		{
			this.regionOptions = await this.regionController.GetAllEntities();

			this.regionsDropdown.AddOptions(this.regionOptions.Select(x => x.name).ToList());
		}

		private void OnDropdownSelected(int index)
		{
			this.selectedRegionIndex = index;
		}

		private async Task OnUserStoredAsync(int storedId)
		{
			this.currentUser = await this.userController.GetEntity(storedId);
			this.OnRegistrationSuccess();
		}

		private void OnSubmitButtonClickedAsync()
		{
			this.CreateUser();
		}

		private async Task CreateUser()
		{
			this.currentUser = await this.userController.CreateEntity(this.ConstructUser(), this.OnRegistrationSuccess, this.OnRegistrationFailure);
			this.registrationPrefsHandler.SaveToPrefs(this.currentUser.pk);
		}

		private void OnRegistrationFailure()
		{
			this.errorMessage.SetActive(true);
		}

		private void OnRegistrationSuccess()
		{
			this.gameObject.SetActive(false);
			this.voteScreen.SetActive(true);
			EventAggregator.Instance.Invoke<UserCreated>(new UserCreated(this.currentUser));
		}

		private User ConstructUser()
		{
			User user = new User();
			user.age = int.Parse(this.ageInput.text);
			user.isOrganizationMember = this.organizationMember.isOn;
			user.name = this.nameInput.text;
			user.passportId = this.passportId.text;
			user.regionPk = (this.selectedRegionIndex + 1);
			return user;
		}
	}
}
