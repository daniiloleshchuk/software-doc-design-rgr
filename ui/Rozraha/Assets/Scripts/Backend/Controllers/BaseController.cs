using Newtonsoft.Json;
using Rozraha.Backend.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace Rozraha.Backend.Controllers
{
	public abstract class BaseController<T> where T : Model
	{
		public abstract string GetAllEntitiesRoute();

		public abstract string GetSpecificEntityRoute(int id);

		public abstract string GetDeleteRoute(int id);

		public abstract string GetEditRoute(T entity);

		public abstract string GetCreateRoute(T entity);


		public async Task<List<T>> GetAllEntities()
		{
			string responseJson = await RequestHandler.Instance.SendRequest(HttpMethod.Get, this.GetAllEntitiesRoute());

			return JsonConvert.DeserializeObject<List<T>>(responseJson);
		}

		public async void DeleteEntity(int id)
		{
			await RequestHandler.Instance.SendRequest(HttpMethod.Delete, this.GetDeleteRoute(id));
		}

		public async Task<T> GetEntity(int id)
		{
			string responseJson = await RequestHandler.Instance.SendRequest(HttpMethod.Get, this.GetSpecificEntityRoute(id));

			return JsonConvert.DeserializeObject<T>(responseJson);
		}

		public async Task<List<T>> GetAllEntitiesById(int id)
		{
			string responseJson = await RequestHandler.Instance.SendRequest(HttpMethod.Get, this.GetSpecificEntityRoute(id));

			return JsonConvert.DeserializeObject<List<T>>(responseJson);
		}

		public async void EditEntity(T entity)
		{
			if (entity != null)
			{
				await RequestHandler.Instance.SendRequest(HttpMethod.Put,
					this.GetEditRoute(entity),
					JsonConvert.SerializeObject(entity));
			}
		}

		public async Task<T> CreateEntity(T entity, Action onSuccess = null, Action onFailure = null)
		{
			if (entity != null)
			{
				string responseJson = await RequestHandler.Instance.SendRequest(HttpMethod.Post,
					this.GetCreateRoute(entity),
					JsonConvert.SerializeObject(entity), onSuccess, onFailure);

				return JsonConvert.DeserializeObject<T>(responseJson);
			}

			return null;
		}
	}
}
