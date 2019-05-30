# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Any, NamedTuple, Optional
from unittest import TestCase


from dazl.rules._rewriter import RewriteContext


class SimpleNode(NamedTuple):
    left: Any
    right: Any


class AnotherSimpleNode(NamedTuple):
    left: Any
    right: Any


class RewriterTest(TestCase):

    def test_double_children(self):
        input_node = SimpleNode(SimpleNode(2, 3), SimpleNode(5, 7))

        rewriter = RewriteContext()
        rewriter.register(int, lambda value: value * 2)
        actual_node = rewriter.rewrite(input_node)

        self.assertEqual(actual_node.left.left, 4)
        self.assertEqual(actual_node.left.right, 6)
        self.assertEqual(actual_node.right.left, 10)
        self.assertEqual(actual_node.right.right, 14)

    def test_unmodified_children(self):
        untouchable_node = SimpleNode('something', SimpleNode('else', 'entirely'))
        input_node = SimpleNode(SimpleNode(2, 3), untouchable_node)

        rewriter = RewriteContext()
        rewriter.register(int, lambda value: value * 2)
        actual_node = rewriter.rewrite(input_node)

        self.assertEqual(actual_node.left.left, 4)
        self.assertEqual(actual_node.left.right, 6)
        self.assertIs(actual_node.right, untouchable_node)

    def test_unmodified_root(self):
        input_node = SimpleNode(SimpleNode(2, 3), SimpleNode(5, 7))

        rewriter = RewriteContext()
        actual_node = rewriter.rewrite(input_node)

        self.assertIs(input_node, actual_node)

    def test_unmodified_root_with_context_objects(self):
        input_node = SimpleNode(SimpleNode(2, 3), SimpleNode(5, 7))

        rewriter = RewriteContext()
        rewriter.context_object(SimpleNode, 'nearest_node')
        actual_node = rewriter.rewrite(input_node)

        self.assertIs(input_node, actual_node)

    def test_context_objects_return_nearest_node(self):
        input_node = SimpleNode(SimpleNode(2, 3), SimpleNode(5, 7))

        def _node_visitor(node: SimpleNode, nearest_node: Optional[SimpleNode]=None):
            if nearest_node is not None:
                self.assertTrue(nearest_node.left is node or nearest_node.right is node)
            return node

        rewriter = RewriteContext()
        rewriter.context_object(SimpleNode, 'nearest_node')
        rewriter.register(SimpleNode, _node_visitor)
        actual_node = rewriter.rewrite(input_node)

        self.assertIs(input_node, actual_node)

    def test_modify_type(self):
        input_node = SimpleNode(SimpleNode(2, 3), SimpleNode(5, 7))

        rewriter = RewriteContext()
        rewriter.register(SimpleNode, lambda node: AnotherSimpleNode(node.left, node.right))

        actual_node = rewriter.rewrite(input_node)

        self.assertIsInstance(actual_node, AnotherSimpleNode)
        self.assertIsInstance(actual_node.left, AnotherSimpleNode)
        self.assertIsInstance(actual_node.right, AnotherSimpleNode)
