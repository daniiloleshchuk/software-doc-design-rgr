using Newtonsoft.Json;
using System.Collections.Generic;

namespace Rozraha.Backend.Models
{
	public class ElectionType : Model
	{
		[JsonProperty("age_from")]
		public int? ageFrom;
		[JsonProperty("age_to")]
		public int? ageTo;
		[JsonProperty("organization_members_only")]
		public bool organizationMembersOnly;
		[JsonProperty("regions_allowed")]
		public List<Region> regionsAllowed;
		[JsonProperty("voter_votes_count")]
		public int votesCount;
		[JsonProperty("votes_cancelable")]
		public bool cancelable;
	}
}