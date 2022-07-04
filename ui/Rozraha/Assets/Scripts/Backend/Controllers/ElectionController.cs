using Rozraha.Backend.Models;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Rozraha.Backend.Controllers
{
	public class ElectionController : BaseController<Election>
	{
		public override string GetAllEntitiesRoute()
		{
			return Routes.LOCALHOST_PREFIX + Routes.ELECTION;
		}

		public override string GetCreateRoute(Election entity)
		{
			return Routes.LOCALHOST_PREFIX + Routes.ELECTION;
		}

		public override string GetDeleteRoute(int id)
		{
			throw new System.NotImplementedException();
		}

		public override string GetEditRoute(Election entity)
		{
			throw new System.NotImplementedException();
		}

		public override string GetSpecificEntityRoute(int id)
		{
			throw new System.NotImplementedException();
		}
	}
}