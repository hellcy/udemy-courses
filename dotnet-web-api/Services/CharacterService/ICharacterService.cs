using System.Collections.Generic;
using System.Threading.Tasks;
using dotnet_web_api.Dtos.Character;
using dotnet_web_api.Models;

namespace dotnet_web_api.Services.CharacterService
{
  public interface ICharacterService
  {
    Task<ServiceResponse<List<GetCharacterDto>>> GetAllCharacters();
    Task<ServiceResponse<GetCharacterDto>> GetCharacterById(int id);
    Task<ServiceResponse<List<GetCharacterDto>>> AddCharacter(AddCharacterDto newCharacter);
    Task<ServiceResponse<GetCharacterDto>> UpdateCharacter(UpdateCharacterDto updatedCharacter);
    Task<ServiceResponse<List<GetCharacterDto>>> DeleteCharacter(int id);
  }
}