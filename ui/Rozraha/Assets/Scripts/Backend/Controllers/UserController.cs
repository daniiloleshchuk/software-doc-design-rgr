using Rozraha.Backend.Models;
using System;

namespace Rozraha.Backend.Controllers
{
	public class UserController : BaseController<User>
	{
		public override string GetAllEntitiesRoute()
		{
			throw new NotImplementedException();
		}

		public override string GetCreateRoute(User entity)
		{
			return Routes.LOCALHOST_PREFIX + Routes.USER;
		}

		public override string GetDeleteRoute(int id)
		{
			throw new NotImplementedException();
		}

		public override string GetEditRoute(User entity)
		{
			throw new NotImplementedException();
		}

		public override string GetSpecificEntityRoute(int id)
		{
			return Routes.LOCALHOST_PREFIX + Routes.USER + $"?pk={id}";
		}
	}
}
