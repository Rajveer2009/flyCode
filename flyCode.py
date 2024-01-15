def text_to_binary_ascii(text):
    binary_strings = []  # Store binary strings for each character
    for char in text:
        ascii_code = ord(char)
        binary_code = format(ascii_code, "08b")
        binary_strings.append(binary_code)
    return binary_strings
def transform_binary_string(binary_strings, flip):
    flip = int(flip)
    transformed_strings = []
    for binary_string in binary_strings:
        transformed_strings.append(binary_string[1:flip] + ("1" if binary_string[flip] == "0" else "0") + binary_string[flip+1:])
    return transformed_strings
def encode(ascii: str, code: str):
    character_to_flip = code
    text = ascii
    binary_ascii_strings = text_to_binary_ascii(text)
    transformed_strings = transform_binary_string(binary_ascii_strings, character_to_flip)
    return "".join(transformed_strings)

def modify_binary_string(input_string, character_to_flip_index):
  """Modifies the string as specified in the prompt, including flipping a specific character."""
  modified_string = ""
  current_group = ""
  for character in input_string:
    current_group += character
    if len(current_group) == 7:
      # Flip the specified character
      current_group = (
          current_group[:int(character_to_flip_index)]
          + ("0" if current_group[int(character_to_flip_index)] == "1" else "1")
          + current_group[int(character_to_flip_index) + 1 :]
      )
      # Add space and modified group
      modified_string += "0" + current_group + " "
      current_group = ""
  # Add remaining characters (may be less than 7)
  if current_group:
    current_group = (
        current_group[:int(character_to_flip_index)]
        + ("0" if current_group[int(character_to_flip_index)] == "1" else "1")
        + current_group[int(character_to_flip_index) + 1 :]
    )  # Flip if needed
    modified_string += "0" + current_group  # Add leading zero if needed
  return modified_string
def split_string_into_list(string_to_split):
  return string_to_split.split(" ")
def decode(binary: str, code: str):
    original_binary_string = binary
    character_to_flip = code
    modified_binary_string = modify_binary_string(original_binary_string, str(int(character_to_flip) - 1))
    text = ""
    for i in range((len(split_string_into_list(modified_binary_string))) - 1):
        binary_string = split_string_into_list(modified_binary_string)[i]
        character = chr(int(binary_string, 2))
        text += character
    return text