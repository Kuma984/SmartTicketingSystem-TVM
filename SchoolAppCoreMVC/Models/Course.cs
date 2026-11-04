using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace SchoolAppCoreMVC.Models
{
    public class Course
    {
        public int CourseID { get; set; }

        [Required]
        [StringLength(100)]
        public string Title { get; set; } = string.Empty;

        public int Credits { get; set; }

        public int DepartmentID { get; set; }

        public Department? Department { get; set; }
        public ICollection<Enrollment> Enrollments { get; set; } = new List<Enrollment>();
    }
}
