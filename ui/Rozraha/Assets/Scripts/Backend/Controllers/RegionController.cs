using Rozraha.Backend.Models;
using System;

namespace Rozraha.Backend.Controllers
{
	public class RegionController : BaseController<Region>
	{
		public override string GetAllEntitiesRoute()
		{
			return Routes.LOCALHOST_PREFIX + Routes.REGION;
		}

		public override string GetCreateRoute(Region entity)
		{
			throw new NotImplementedException();
		}

		public override string GetDeleteRoute(int id)
		{
			return Routes.LOCALHOST_PREFIX + Routes.REGION	+ $"?pk={id}";
		}

		public override string GetEditRoute(Region entity)
		{
			throw new NotImplementedException();
		}

		public override string GetSpecificEntityRoute(int id)
		{
			throw new NotImplementedException();
		}
	}
}
