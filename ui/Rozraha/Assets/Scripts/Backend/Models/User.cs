using Newtonsoft.Json;

namespace Rozraha.Backend.Models
{
	public class User : Model
	{
		[JsonProperty("region_pk")]
		public int regionPk;
		public string name;
		public int age;
		[JsonProperty("is_organization_member")]
		public bool isOrganizationMember;
		[JsonProperty("passport_id")]
		public string passportId;
	}
}
