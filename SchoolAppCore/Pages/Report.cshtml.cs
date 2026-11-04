using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using SchoolAppCore.Models;

namespace SchoolAppCore.Pages
{
    public class ReportModel : PageModel
    {
        private readonly SchoolContext _context;

        public ReportModel(SchoolContext context)
        {
            _context = context;
        }

        public int TotalStudents { get; set; }
        public int TotalCourses { get; set; }
        public int TotalInstructors { get; set; }
        public int TotalDepartments { get; set; }
        public int TotalEnrollments { get; set; }
        public decimal AverageGrade { get; set; }

        public IList<Enrollment> RecentEnrollments { get; set; } = new List<Enrollment>();

        public async Task OnGetAsync()
        {
            TotalStudents = await _context.Students.CountAsync();
            TotalCourses = await _context.Courses.CountAsync();
            TotalInstructors = await _context.Instructors.CountAsync();
            TotalDepartments = await _context.Departments.CountAsync();
            TotalEnrollments = await _context.Enrollments.CountAsync();

            var grades = await _context.Enrollments.Where(e => e.Grade.HasValue).Select(e => e.Grade!.Value).ToListAsync();
            AverageGrade = grades.Any() ? grades.Average() : 0.0m;

            RecentEnrollments = await _context.Enrollments
                .Include(e => e.Student)
                .Include(e => e.Course)
                .OrderByDescending(e => e.EnrollmentID)
                .ToListAsync();
        }
    }
}
