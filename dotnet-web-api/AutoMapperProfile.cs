using AutoMapper;
using dotnet_web_api.Dtos.Character;
using dotnet_web_api.Models;

namespace dotnet_web_api
{
  public class AutoMapperProfile : Profile
  {
    public AutoMapperProfile()
    {
      // first argument: source type
      // second argument: destination type
      CreateMap<Character, GetCharacterDto>();
      CreateMap<AddCharacterDto, Character>();
    }
  }
}