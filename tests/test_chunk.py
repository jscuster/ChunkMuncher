import unittest
import sys
import struct
from pathlib import Path

pkgPath = Path.cwd().parent / 'src' # long way of getting to ../src, but this way gets the full path, and is the suggested way in the python docs.
pkgPath = str(pkgPath) #all that for a string?!
# Some modules don't handle Path objects. Hoping to have that fixed soon, but not until what's here has working tests.
#append the path to the module under test.
if not pkgPath in sys.path: sys.path.append(pkgPath) # path to module being tested.
from chunkmuncher import chunk

class test_chunk_midi(unittest.TestCase):
	"""Test the chunk module."""
	# Define the bytes of a midi file in hex, kept in memory.
	midiData = (
		b'MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x01'
		b'MTrk\x00\x00\x00\x24\x00\xb0\x07\x64\x00\xc0\x00\x00\x90\x3c\x64\x00\x90\x40\x64\x00\x90\x43\x64'
		b'\x03\x00\x80\x3c\x00\x00\x80\x40\x00\x00\x80\x43\x00\x00\xff\x2f\x00'
	)

	#helper functions to create then delete a midi file.
	def makeMidiFile(self):
		"""Write a MIDI file that plays a C major chord for 3 seconds."""
		#define path of midi file.
		self.path = Path.cwd() / 'tmp.mid'
		# Save the MIDI data to a file
		self.path.write_bytes(self.midiData)
		return self.path

	def delMid(self):
		if self.path.exists():
			self.path.unlink()
			self.path=None

	def test_read_chunks(self):
		midFile = self.makeMidiFile() # midFile: is the Path to written midi.
		file = open(midFile, "rb")
		# Read the header chunk
		header = chunk.Chunk(file, bigendian=True)
		self.assertEqual(header.getname(), b'MThd')
		# Read the header chunk data
		header_data = header.read()
		format_type, num_tracks, division = struct.unpack(">HHH", header_data[:6])
		self.assertEqual(format_type, 0)
		self.assertEqual(num_tracks, 1)
		self.assertEqual(division, 1)
		# Read the track chunk
		track = chunk.Chunk(file, bigendian=True)
		self.assertEqual(track.getname(), b'MTrk')
		# Read the track chunk data
		track_data = track.read()
		# Skip to the next chunk (if there is padding)
		track.skip()
		file.close()
		self.delMid() #delete the temporary file.
		midiData = self.midiData
		#make sure the track that was written is what was read.
		self.assertTrue(track_data in midiData)
		self.assertEqual(midiData.index(track_data), 22)

if __name__ == '__main__': unittest.main()
