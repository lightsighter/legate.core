# Copyright 2021 NVIDIA Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import, division, print_function

# Import select types for Legate library construction
from legate.core.context import ResourceConfig
from legate.core.legate import (
    Array,
    Library,
)
from legate.core.runtime import (
    get_legate_runtime,
    get_legion_context,
    get_legion_runtime,
    legate_add_library,
)
from legate.core.store import ExternalAllocation, Store
from legate.core.legion import (
    LEGATE_MAX_DIM,
    LEGATE_MAX_FIELDS,
    Point,
    Rect,
    Domain,
    Transform,
    AffineTransform,
    IndexSpace,
    PartitionFunctor,
    PartitionByRestriction,
    PartitionByImage,
    PartitionByImageRange,
    EqualPartition,
    PartitionByWeights,
    IndexPartition,
    FieldSpace,
    FieldID,
    Region,
    Partition,
    Fill,
    IndexFill,
    Copy,
    IndexCopy,
    Attach,
    Detach,
    Acquire,
    Release,
    Future,
    OutputRegion,
    PhysicalRegion,
    InlineMapping,
    Task,
    FutureMap,
    IndexTask,
    Fence,
    ArgumentMap,
    BufferBuilder,
    legate_task_preamble,
    legate_task_progress,
    legate_task_postamble,
)
from legate.core.types import (
    bool_,
    int8,
    int16,
    int32,
    int64,
    uint8,
    uint16,
    uint32,
    uint64,
    float16,
    float32,
    float64,
    complex64,
    complex128,
    ReductionOp,
)
from legion_cffi import ffi, lib as legion

# Import the PyArrow type system
from pyarrow import (
    DataType,
    DictionaryType,
    ListType,
    MapType,
    StructType,
    UnionType,
    TimestampType,
    Time32Type,
    Time64Type,
    FixedSizeBinaryType,
    Decimal128Type,
    Field,
    Schema,
    null,
    time32,
    time64,
    timestamp,
    date32,
    date64,
    binary,
    string,
    utf8,
    large_binary,
    large_string,
    large_utf8,
    decimal128,
    list_,
    large_list,
    map_,
    struct,
    dictionary,
    field,
    schema,
    from_numpy_dtype,
)
