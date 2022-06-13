using Newtonsoft.Json;

namespace Rozraha.Backend.Models
{
	public class CandidateWithStats : Model
	{
		public User candidate;
		[JsonProperty("total_votes")]
		public int totalVotes;
	}
}
