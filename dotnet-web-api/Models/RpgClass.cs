using System.Text.Json.Serialization;

namespace dotnet_web_api.Models
{
  [JsonConverter(typeof(JsonStringEnumConverter))]
  public enum RpgClass 
  {
    Knight,
    Mage,
    Cleric,
  }
}