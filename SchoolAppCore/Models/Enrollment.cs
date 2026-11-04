using System.ComponentModel.DataAnnotations;

namespace SchoolAppCore.Models
{
    public class Enrollment
    {
        public int EnrollmentID { get; set; }

        public int CourseID { get; set; }

        public int StudentID { get; set; }

        [Range(0.0, 4.0)]
        public decimal? Grade { get; set; }

        public Course? Course { get; set; }
        public Student? Student { get; set; }
    }
}
