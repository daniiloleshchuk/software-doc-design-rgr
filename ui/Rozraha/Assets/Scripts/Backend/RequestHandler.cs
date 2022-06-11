using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;

namespace Rozraha.Backend
{
	public class RequestHandler
	{
		private const string WEB_JSON_TYPE = "application/json";
		private const string PATH = "Configs/";

		private HttpClient client;

		public string Config { get; private set; }

		private static RequestHandler instance;
		public static RequestHandler Instance
		{
			get
			{
				if (instance == null)
				{
					instance = new RequestHandler();
				}
				return instance;
			}
		}

		private RequestHandler()
		{

		}

		public async Task<string> SendRequest(HttpMethod method, string uri, string data = null, Action onSuccess = null, Action onFailure = null)
		{
			this.client = new HttpClient();

			HttpRequestMessage request = new HttpRequestMessage(method, uri);

			if (!string.IsNullOrEmpty(data))
			{
				request.Content = new StringContent(data, Encoding.UTF8, WEB_JSON_TYPE);
			}

			request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue(WEB_JSON_TYPE));

			try
			{
				HttpResponseMessage response = await this.client.SendAsync(request);
				string content = await response.Content.ReadAsStringAsync();
				Debug.Log(response.StatusCode);

				if (response.StatusCode is System.Net.HttpStatusCode.OK or System.Net.HttpStatusCode.Created or System.Net.HttpStatusCode.Accepted && onSuccess != null)
				{
					onSuccess();
				}
				else if (onFailure != null)
				{
					onFailure();
				}
				return content;
			}
			catch (ArgumentException argExp)
			{
				Debug.Log(argExp);

				if (onFailure != null)
				{
					onFailure();
				}

				return null;
			}
		}

		private void DeserializeConfig(string name)
		{
			this.Config = Resources.Load<TextAsset>(PATH + name).text;

			try
			{
				//this.Config = JsonConvert.DeserializeObject<GeneralConfig>(jsonString);
			}
			catch (Exception e)
			{
				Debug.LogError(e.Message);
			}
		}
	}
}
