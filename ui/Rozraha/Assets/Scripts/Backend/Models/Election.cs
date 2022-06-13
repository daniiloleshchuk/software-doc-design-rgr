using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using UnityEngine;

namespace Rozraha.Backend.Models
{
	public class Election : Model
    {
        public List<User> candidates;
        public DateTime end;
        public DateTime start;
        public ElectionType type;

        [JsonIgnore]
        public bool voted;

        public void CheckVotedStatus()
		{
            this.voted = Convert.ToBoolean(int.Parse(PlayerPrefs.GetString(this.pk.ToString(), "0")));
		}
    }
}