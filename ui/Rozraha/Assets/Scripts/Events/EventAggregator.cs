using System.Collections.Generic;
using UnityEngine;
using System;

namespace Rozraha.Events
{
	public class EventAggregator
	{
		private Dictionary<Type, Action<EventArgs>> events = new Dictionary<Type, Action<EventArgs>>();
		private Dictionary<Delegate, Action<EventArgs>> eventLookups = new Dictionary<Delegate, Action<EventArgs>>();

		private static EventAggregator instance;
		public static EventAggregator Instance
		{
			get
			{
				if (instance == null)
				{
					instance = new EventAggregator();
				}
				return instance;
			}
		}

		private EventAggregator()
		{

		}

		public void Subscribe<T>(Action<T> listener) where T : EventArgs
		{
			Type type = typeof(T);

			if (listener == null)
			{
				Debug.LogError($"EventAggregator.Subscribe<{type.Name}>() Argument is null!");
				return;
			}

			if (this.eventLookups.ContainsKey(listener))
			{
				return;
			}

			Action<EventArgs> newAction = e => listener((T)e);
			this.eventLookups[listener] = newAction;

			if (this.events.ContainsKey(type))
			{
				this.events[type] += newAction;
			}
			else
			{
				this.events.Add(type, newAction);
			}
		}

		public void Unsubscribe<T>(Action<T> listener) where T : EventArgs
		{
			Type type = typeof(T);

			if (listener == null)
			{
				Debug.LogError($"EventAggregator.Unsubscribe<{type.Name}>() Argument is null!");
				return;
			}

			if (!this.eventLookups.TryGetValue(listener, out Action<EventArgs> removedAction))
			{
				return;
			}

			if (this.events.ContainsKey(type))
			{
				this.events[type] -= removedAction;
				if (this.events[type] == null)
				{
					this.events.Remove(type);
				}
			}

			this.eventLookups.Remove(listener);
		}

		/// <summary>
		/// Invoke a list of all subscripted methods for specific event type
		/// </summary>
		/// <typeparam name="T">Class where subscription is performer</typeparam>
		/// <param name="args">Event related data, generic variative</param>
		public void Invoke<T>(EventArgs args = default)
		{
			Type type = typeof(T);

			this.events[type]?.Invoke(args);
		}
	}
}

