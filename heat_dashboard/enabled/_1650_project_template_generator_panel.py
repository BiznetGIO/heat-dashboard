#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

import heat_dashboard

from horizon.utils.file_discovery import discover_files

# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'template_generator'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'orchestration'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'heat_dashboard.content.template_generator.panel.TemplateGenerator'

# Automatically discover static resources in installed apps

ADD_ANGULAR_MODULES = \
    ['horizon.dashboard.project.heat_dashboard.template_generator']

AUTO_DISCOVER_STATIC_FILES = True

TEMPLATE_GENERATOR_BASE = 'dashboard/project/heat_dashboard/template_generator'
CSS_BASE = '%s/css' % TEMPLATE_GENERATOR_BASE
JS_BASE = '%s/js' % TEMPLATE_GENERATOR_BASE

ADD_SCSS_FILES = [
    '%s/hotgen-hotgen-main.scss' % CSS_BASE,
    'horizon/lib/font_awesome/scss/font-awesome.scss']

HEAT_DASHBOARD_ROOT = heat_dashboard.__path__[0]

ADD_JS_FILES = discover_files(os.path.join(HEAT_DASHBOARD_ROOT, 'static'),
                              sub_path='%s/vendors' % JS_BASE,
                              ext='.js', trim_base_path=True)
ADD_JS_FILES.extend([
    '%s/components/template-generator.module.js' % JS_BASE,
    '%s/components/utils.module.js' % JS_BASE,
    '%s/components/agent.module.js' % JS_BASE,
])

ADD_JS_FILES.extend(
    [file for file in discover_files(
        os.path.join(HEAT_DASHBOARD_ROOT,
                     'static'),
        sub_path='%s/components' % JS_BASE,
        ext='.js',
        trim_base_path=True)
        if file not in ADD_JS_FILES and 'spec.js' not in file
     ])
ADD_JS_FILES.extend(
    [file for file in discover_files(
        os.path.join(HEAT_DASHBOARD_ROOT, 'static'),
        sub_path='%s/resources' % JS_BASE,
        ext='.js', trim_base_path=True) if 'spec.js' not in file
     ])
