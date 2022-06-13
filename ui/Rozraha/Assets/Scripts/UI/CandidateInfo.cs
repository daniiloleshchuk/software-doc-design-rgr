namespace Rozraha.UI
{
	public struct CandidateInfo
	{
		public string name;

		public string region;

		public int votesCount;

		public CandidateInfo(string name, string region, int votesCount)
		{
			this.name = name;
			this.region = region;
			this.votesCount = votesCount;
		}
	}
}
