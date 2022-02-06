# import jack
import jack

midiInBuffer = []
midiOutBuffer = []

client = jack.Client('jack')

midi_in = client.midi_inports.register('midi_in')
midi_out = client.midi_outports.register('midi_out')

@client.set_process_callback

def process(frames):

  midi_out.clear_buffer()
  if (len(midiOutBuffer)):
    for msg in midiOutBuffer:
      midi_out.write_midi_event(0, msg)
      print('MIDI sent = ', msg)
  midiOutBuffer.clear()

  for offset, data in midi_in.incoming_midi_events():
    msg = struct.unpack('3B', data)
    midiInBuffer.append(msg)
    print('MIDI rcvd = ', msg)

client.activate()

print(client.midi_inports)
print(client.midi_outports)

# forward all incoming messages from midi_in to midi_out
while True:
  for msg in midiInBuffer:
    midiOutBuffer.append(msg)
    print('MIDI fwd = ', msg)
  midiInBuffer.clear()