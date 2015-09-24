#  __author__ = 'Chris Hyde'

# Required import to handle command line arguments
import sys

def main():
    # Get arguments
    input_path, output_path = get_arguments()

    # Get input data
    pather_matrix = get_input_data(input_path)

    # Initialize list to hold hashes found
    hashes_list = find_those_hashes( pather_matrix )

    # Connect those hashes!!!
    pather_matrix = connect_the_hashes( pather_matrix, hashes_list )

    # Write updated pather_matrix to file
    write_to_output_path(pather_matrix, output_path)

def get_arguments():
    # Validate the correct number of arguments were provided
    if( len(sys.argv) != 3 ):
        print('Please ensure you have provided the necessary arguments.')
        sys.exit(1)

    # Return input and output paths
    return sys.argv[1], sys.argv[2]

def get_input_data(input_path):
    # Initialize matrix to hold input data
    pather_matrix = []

    # Read in data from input file into matrix
    try:
        with open( input_path, 'r' ) as input_file:
            for line in input_file.readlines():
                split_line = []
                for character in line.strip():
                    split_line.append( character )

                pather_matrix.append( split_line )

        # Return data matrix
        return pather_matrix

    except:
        print("Something went wrong while trying to find/read ")
        sys.exit(1)

def find_those_hashes(pather_matrix):
     # Initialize list to hold hashes found
    hashes = []

    # Find hashes in matrix
    for x in range( len( pather_matrix ) ):
        for y in range( len( pather_matrix[x] ) ):
            if( pather_matrix[x][y] == '#' ):
                hash = x,y
                hashes.append( hash )

    # Return hash coordinates
    return hashes

def connect_the_hashes( pather_matrix, hashes_list ):
    # While hashes are not connected
    while len( hashes_list ) > 1:
        # Determine starting x position
        starting_x = hashes_list[0][0]

        # Determine starting y position
        starting_y = hashes_list[0][1]

        # Determine differences between vertical coordinates
        vertical_difference = hashes_list[1][0] - hashes_list[0][0]

        # Determine differences between horizontal coordinates
        horizontal_difference = hashes_list[1][1] - hashes_list[0][1]

        # Draw vertical *
        if( vertical_difference > 0 ):
            for x in range( 1, vertical_difference + 1 ):
                pather_matrix[ starting_x + x ][ starting_y ] = '*'

        # Draw horizontal *
        if( horizontal_difference != 0 ):
            for x in range( min( horizontal_difference + 1, 1), max(horizontal_difference, 1 ) ):
                pather_matrix[ starting_x + vertical_difference ][ starting_y + x ] = '*'

        # Remove first hash coordinates from hash list
        hashes_list = hashes_list[1:]

    # Return updated matrix
    return pather_matrix

def write_to_output_path(pather_matrix, output_path):
    # Open Output File and write pather_matrix contents
    with open( output_path, 'w' ) as output_file:
        for line in pather_matrix:
            output_file.write(''.join(line)+'\n')

main()