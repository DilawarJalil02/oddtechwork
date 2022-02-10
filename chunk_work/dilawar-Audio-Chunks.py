import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


# ARI10-1635780311.5068-in.wav yahan se error aya ha

# 25216

# name_list = os.listdir('C:/Users/trainee9/Desktop/Sohaib/T_1')  r"Z:\audios\T_1"
source ='Z:/audios/T_1/'
audio_file_name_list = os.listdir(source)
count = 99007 #95194
main_dir = "C:/Users/trainee6/Desktop/Abdullah/audio_chunks_T_1/"


def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)


audio_file_name_list_2 = audio_file_name_list[99007:]


# for name in name_list:
for file_name in audio_file_name_list_2:
    
    try:
#         count = count +1
#         sound_file = AudioSegment.from_wav(os.path.join(source ,str(name)))
#         audio_chunks = split_on_silence(sound_file, min_silence_len=1900, silence_thresh=-35,  keep_silence=20 )
#         name = name.replace('.wav','')
#         for i, chunk in enumerate(audio_chunks):
#             out_file =os.path.join(main_dir, str(count)+name+"-{0}.wav".format(i+1))
#             print("exporting", out_file)
#             if not os.path.exists(main_dir):
#                 os.mkdir(main_dir)
#             chunk.export(out_file, format="wav")



        # Load your audio.
        song = AudioSegment.from_wav(os.path.join(source ,str(file_name)))

        # Split track where the silence is 2 seconds or more and get chunks using 
        # the imported function.
        chunks = split_on_silence (
            # Use the loaded audio.
            song, 
            # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
            min_silence_len = 1800, #1800
            # Consider a chunk silent if it's quieter than -16 dBFS.
            # (You may want to adjust this parameter.)
            silence_thresh = song.dBFS, #-27

            keep_silence=300,

            seek_step=1
        )

        file_name = file_name.replace('.wav', '')
        
        print('Audio File # ' ,count)
        count+=1
        
        # Process each chunk with your parameters
        for i, chunk in enumerate(chunks):
            # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
            silence_chunk = AudioSegment.silent(duration=500)

            # Add the padding chunk to beginning and end of the entire chunk.
            audio_chunk = silence_chunk + chunk + silence_chunk

            # Normalize the entire chunk.
            normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

            # Export the audio chunk with new bitrate.
            print("Exporting" + file_name + "-{0}.wav".format(i))
            normalized_chunk.export(
                # Z:/Abdullah/audio_chunks_T_1/
                "Z:/Abdullah/audio_chunks_T_1/" + file_name + "-{0}.wav".format(i+1),
                bitrate = "192k",
                format = "wav"
            )
            
        if count%10000==0:
            print("*"*30)
            print(count)
            
            
    except Exception as e:
        print(e)

