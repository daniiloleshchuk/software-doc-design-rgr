using Rozraha.Backend.Models;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Rozraha.Backend.Controllers
{
	public class VoteController : BaseController<Vote>
	{
		public override string GetAllEntitiesRoute()
		{
			throw new System.NotImplementedException();
		}

		public override string GetCreateRoute(Vote entity)
		{
			return Routes.LOCALHOST_PREFIX + Routes.VOTE;
		}

		public override string GetDeleteRoute(int id)
		{
			throw new System.NotImplementedException();
		}

		public override string GetEditRoute(Vote entity)
		{
			throw new System.NotImplementedException();
		}

		public override string GetSpecificEntityRoute(int id)
		{
			throw new System.NotImplementedException();
		}
	}
}