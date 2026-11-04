using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SchoolAppCoreMVC.Models;

namespace SchoolAppCoreMVC.Controllers
{
    public class ReportController : Controller
    {
        private readonly SchoolContext _context;

        public ReportController(SchoolContext context)
        {
            _context = context;
        }

        public async Task<IActionResult> Index()
        {
            var model = new ReportViewModel
            {
                TotalStudents = await _context.Students.CountAsync(),
                TotalCourses = await _context.Courses.CountAsync(),
                TotalInstructors = await _context.Instructors.CountAsync(),
                TotalDepartments = await _context.Departments.CountAsync(),
                TotalEnrollments = await _context.Enrollments.CountAsync(),
                AverageGrade = await _context.Enrollments
                    .Where(e => e.Grade.HasValue)
                    .Select(e => e.Grade!.Value)
                    .DefaultIfEmpty(0)
                    .AverageAsync(),
                RecentEnrollments = await _context.Enrollments
                    .Include(e => e.Student)
                    .Include(e => e.Course)
                    .OrderByDescending(e => e.EnrollmentID)
                    .Take(5)
                    .ToListAsync()
            };
            return View(model);
        }
    }

    public class ReportViewModel
    {
        public int TotalStudents { get; set; }
        public int TotalCourses { get; set; }
        public int TotalInstructors { get; set; }
        public int TotalDepartments { get; set; }
        public int TotalEnrollments { get; set; }
        public decimal AverageGrade { get; set; }
        public List<Enrollment> RecentEnrollments { get; set; } = new();
    }
}
