/*
 * Copyright (c) 2015 Ken Robbins
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

#ifndef DOCSTRINGS_H_
#define DOCSTRINGS_H_

static const char* rapidjson_module_docstring =
    "Fast, simple JSON encoder and decoder. Based on RapidJSON C++ library.";

static const char* rapidjson_loads_docstring =
    "loads(s, object_hook=None, use_decimal=False, precise_float=True, allow_nan=True)\n\nDecodes a JSON string into Python object.";

static const char* rapidjson_dumps_docstring =
    "dumps(obj, skipkeys=False, ensure_ascii=True, allow_nan=True, indent=None, default=None, sort_keys=False, use_decimal=False, max_recursion_depth=2048, datetime_mode=None)\n\nEncodes Python object into a JSON string.";

#endif
