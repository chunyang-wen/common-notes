#!/usr/bin/env python
# coding: utf-8


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import sys

from google.protobuf import text_format

from tensorflow.core.framework import graph_pb2
from tensorflow.python.platform import app
from tensorflow.python.platform import flags
from tensorflow.python.platform import gfile

FLAGS = flags.FLAGS

flags.DEFINE_string("graph", "", """TensorFlow 'GraphDef' file to load.""")
flags.DEFINE_bool("input_binary", True,
                  """Whether the input files are in binary format.""")
flags.DEFINE_string("dot_output", "", """Where to write the DOT output.""")


def main(unused_args):
  if not gfile.Exists(FLAGS.graph):
    print("Input graph file '" + FLAGS.graph + "' does not exist!")
    return -1

  graph = graph_pb2.GraphDef()
  with open(FLAGS.graph, "r") as f:
    if FLAGS.input_binary:
      graph.ParseFromString(f.read())
    else:
      text_format.Merge(f.read(), graph)

  with open(FLAGS.dot_output, "wb") as f:
    print("digraph graphname {", file=f)
    for node in graph.node:
      output_name = node.name
      print("  \"" + output_name + "\" [label=\"" + node.op + "\"];", file=f)
      for input_full_name in node.input:
        print(input_full_name, file=sys.stderr)
        parts = input_full_name.split(":")
        input_name = re.sub(r"^\^", "", parts[0])
        print("  \"" + input_name + "\" -> \"" + output_name + "\";", file=f)
    print("}", file=f)
  print("Created DOT file '" + FLAGS.dot_output + "'.")


if __name__ == "__main__":
  app.run()

