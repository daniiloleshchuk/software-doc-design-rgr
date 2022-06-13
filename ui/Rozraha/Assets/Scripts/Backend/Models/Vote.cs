using Newtonsoft.Json;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Rozraha.Backend.Models
{
	public class Vote : Model
	{
		[JsonProperty("voting_data")]
		public Dictionary<int, int> votingData;
		[JsonProperty("voter_id")]
		public int voterId;
		[JsonProperty("election_id")]
		public int electionId;
		[JsonProperty("election_pk")]
		public int electionPk;
		[JsonProperty("region_id")]
		public int regionId;
	}
}