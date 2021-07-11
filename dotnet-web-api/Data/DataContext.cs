using dotnet_web_api.Models;
using Microsoft.EntityFrameworkCore;

namespace dotnet_web_api.Data
{
  public class DataContext : DbContext
  {
    public DataContext(DbContextOptions<DataContext> options) : base(options)
    {

    }

    public DbSet<Character> Characters { get; set; }
  }
}