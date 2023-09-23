import argparse
import os

PODCAST = '''
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
    <channel>
        <title>Empty Podcast {counter}</title>
        <description>Empty Podcast {counter}</description>
        <itunes:image href="{logo}" />
        <item>
            <title>Dummy Episode (Archive it)</title>
            <description>Some podcast apps only accept podcasts containing at least one episode</description>
            <enclosure url="https://raw.githubusercontent.com/mehdi-behrooz/empty-podcasts/main/resources/fake.mp3" type="audio/mpeg" length="40554"/>
            <itunes:duration>9</itunes:duration>
            <pubDate>Wed, 01 Jan 2020 00:00:00 GMT</pubDate>
        </item>
    </channel>
</rss>
'''

PREDEFINED_LOGOS = {
    "white": "https://raw.githubusercontent.com/mehdi-behrooz/empty-podcasts/main/resources/white.png",
    "black": "https://raw.githubusercontent.com/mehdi-behrooz/empty-podcasts/main/resources/black.png"
}

def run(number, logo, output_directory):
    
    # break if input number is negative
    if number <= 0:
        return
        
    # number of digits for zero padding
    max_digits = len(str(number))
       
    # calculate logo url
    logo = logo.strip()
    logo = PREDEFINED_LOGOS[logo] if logo.lower() in PREDEFINED_LOGOS else logo
       
    # make output directory
    os.makedirs(output_directory, exist_ok=True)

    # create rss files one by one
    for i in range(number):
    
        # zero-padded podcast number
        counter = str(i + 1).zfill(max_digits)
        
        # generate podcast rss 
        podcast = PODCAST.format(counter=counter, logo=logo)

        # remove empty lines
        podcast = "".join([s for s in podcast.splitlines(True) if s.strip("\r\n")])

        # write rss content to the output file
        output = os.path.join(output_directory, f"{counter}.rss")
        with open(output, 'w') as f:
            print(podcast, file=f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates empty podcasts.")
    parser.add_argument('-n', '--number', type=int, required=False, default=10, help='number of podcasts')
    parser.add_argument('-l', '--logo', required=False, default='white', help='either black, white, or any custom logo web url')
    parser.add_argument('-o', '--output-directory', required=False, default='dist', help='output directory')
    args = parser.parse_args()
    run(args.number, args.logo, args.output_directory)