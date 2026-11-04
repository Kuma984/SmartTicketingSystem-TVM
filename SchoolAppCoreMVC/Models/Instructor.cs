using System;
using System.ComponentModel.DataAnnotations;

namespace SchoolAppCoreMVC.Models
{
    public class Instructor
    {
        public int InstructorID { get; set; }

        [Required]
        [StringLength(50)]
        public string FirstName { get; set; } = string.Empty;

        [Required]
        [StringLength(50)]
        public string LastName { get; set; } = string.Empty;

        [DataType(DataType.Date)]
        public DateTime HireDate { get; set; }
    }
}
