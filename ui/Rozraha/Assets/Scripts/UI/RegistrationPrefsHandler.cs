using UnityEngine;

namespace Rozraha.UI
{
	public class RegistrationPrefsHandler
	{
		private const string REGISTERED_KEY = "Registered_";

		public void SaveToPrefs(int value)
		{
			PlayerPrefs.SetInt(REGISTERED_KEY, value);
		}

		public int LoadFromPrefs()
		{
			return PlayerPrefs.GetInt(REGISTERED_KEY, 0);
		}
	}
}
