def new_line(string):
    print(f'''
{string}''')

def new_line_input(string):
    return str(input(f'''
{string}
>> '''))

def print_logo():
    print('''                                                                            
    ***** ***                                                               
******  * **  *                                            *               
**   *  *  ** ***                                          ***              
*    *  *   **  *                                            *               
    *  *    *                          ****   ***  ****                      
** **   *  ***   *** **** ****     * ***  * **** **** * ***       ****    
** **  *    ***   *** **** ***  * *   ****   **   ****   ***     * ***  * 
** ****      **    **  **** **** **    **    **           **    *   ****  
** **  ***   **    **   **   **  **    **    **           **   **    **   
** **    **  **    **   **   **  **    **    **           **   **    **   
*  **    **  **    **   **   **  **    **    **           **   **    **   
    *     **  **    **   **   **  **    **    **           **   **    **   
****      *** **    **   **   **   ******     ***          **   **    **   
*  ****    **  *** * ***  ***  ***   ****       ***         *** * ***** **  
*    **     *    ***   ***  ***  ***                          ***   ***   ** 
*                                                                            
**                 A text-based adventure game in Python                 
''')

def print_map(current_location, world_map, animals):
    # Must be odd
    map_width, map_height = 9, 7
    row = build_map_divider(map_width)
    output = '\n'
    output += row
    location = current_location.split(',')
    x, y = int(location[0]), int(location[1])
    map_x = x - (map_width // 2)
    map_y = y + (map_height // 2)

    for ly in range(map_height):
        for lx in range(map_width):
            coordinates = f'{map_x + lx},{map_y - ly}'
            output += '┆ '
            if coordinates in world_map:
                if coordinates == current_location:
                    # X marks the spot
                    output += '★'
                else:
                    # Returns first letter of terrain type
                    output += world_map[coordinates].type[0].upper()
            else:
                # Blank if undiscovered
                output += ' '
            if coordinates == '0,0':
                # Trailing asterisk if origin
                output += '°'
            elif coordinates in animals and animals[coordinates]:
                output += '‡'
            else:
                # Trailing blank for spacing
                output += ' '
        output += f'┆\n{row}'
    
    output += '''  ↑
  N    Key: ★ - Current location
            A - Terrain type
              - Undiscovered terrain
            ° - Origin (0,0)
            ‡ - Location with animal'''

    return print(output)

def build_map_divider(width):
    output = ' '
    for _ in range(width):
        output += '--- '
        if _ == width - 1:
            output += '\n'
    return output