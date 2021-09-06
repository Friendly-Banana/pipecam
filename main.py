import cv2
import mediapipe as mp

config_text = """
  input_stream: 'in_stream'
  output_stream: 'out_stream'
  node {
    calculator: 'PassThroughCalculator'
    input_stream: 'in_stream'
    output_stream: 'out_stream'
  }
"""
graph = mp.CalculatorGraph(graph_config=config_text)
output_packets = []
graph.observe_output_stream(
    'out_stream',
    lambda stream_name, packet:
        output_packets.append(mp.packet_getter.get_str(packet)))

graph.start_run()

graph.add_packet_to_input_stream(
    'in_stream', mp.packet_creator.create_str('abc').at(0))

rgb_img = cv2.cvtColor(cv2.imread('/path/to/your/image.png'), cv2.COLOR_BGR2RGB)
graph.add_packet_to_input_stream(
    'in_stream',
    mp.packet_creator.create_image_frame(format=mp.ImageFormat.SRGB,
                                         data=rgb_img).at(1))

graph.close()