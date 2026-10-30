namespace TVM_Demo.Models
{
    /// <summary>
    /// Represents a transit destination and its corresponding flat fare.
    /// </summary>
    public class Destination
    {
        public int DestinationID { get; set; }
        public string Name { get; set; } = string.Empty;
        public decimal Fare { get; set; }

        public override string ToString()
        {
            return $"{Name} - {Fare:N0} VND";
        }
    }
}
