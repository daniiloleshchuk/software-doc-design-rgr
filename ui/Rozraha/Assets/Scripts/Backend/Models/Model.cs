using Newtonsoft.Json;

namespace Rozraha.Backend.Models
{
	public class Model
	{
		[JsonIgnore]

		public int pk;

		[JsonProperty("pk")]
		private int ObsoleteSettingAlternateSetter
		{
			set { pk = value; }
		}
	}
}
