using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace SchoolAppCore.Models
{
    public class Department
    {
        public int DepartmentID { get; set; }

        [Required]
        [StringLength(50)]
        public string Name { get; set; } = string.Empty;

        [DataType(DataType.Currency)]
        public decimal Budget { get; set; }

        [DataType(DataType.Date)]
        public DateTime StartDate { get; set; }

        public ICollection<Course> Courses { get; set; } = new List<Course>();
    }
}
