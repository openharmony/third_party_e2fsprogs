/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __DAC_CONFIG
#define __DAC_CONFIG
#include <stdint.h>

#ifdef __cpluscplus
extern "C" {
#endif

int LoadDacConfig(const char* fn);
void GetDacConfig(const char* path, int dir, char* targetOutPath,
        unsigned* uid, unsigned* gid, unsigned* mode,
        uint64_t* capabilities);

#ifdef __cpluscplus
}
#endif
#endif
