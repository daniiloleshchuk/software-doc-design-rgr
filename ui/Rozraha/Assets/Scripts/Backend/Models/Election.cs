using System;
using System.Collections.Generic;

namespace Rozraha.Backend.Models
{
	public class Election : Model
    {
        public List<User> candidates;
        public DateTime end;
        public DateTime start;
        public ElectionType type;
    }
}