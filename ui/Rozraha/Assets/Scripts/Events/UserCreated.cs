using System;
using Rozraha.Backend.Models;

namespace Rozraha.Events
{
	public class UserCreated : EventArgs
	{
		public User user;

		public UserCreated(User user)
		{
			this.user = user;
		}
	}
}

