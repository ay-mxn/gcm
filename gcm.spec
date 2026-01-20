# -*- mode: python ; coding: utf-8 -*-
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
"""
PyInstaller spec file for GCM (GPU Cluster Monitoring) CLI.
"""
import os
from pathlib import Path

block_cipher = None

# Read version from version.txt
version_file = Path('gcm/version.txt')
if version_file.exists():
    version = version_file.read_text().strip()
else:
    version = os.environ.get('GCM_VERSION', 'unknown')

# Set version in environment for runtime
os.environ['GCM_VERSION'] = version

a = Analysis(
    ['gcm/monitoring/cli/gcm.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('gcm/version.txt', 'gcm'),
        ('gcm/py.typed', 'gcm'),
    ],
    hiddenimports=[
        'gcm',
        'gcm._version',
        'gcm.monitoring',
        'gcm.monitoring.cli',
        'gcm.monitoring.cli.nvml_monitor',
        'gcm.monitoring.cli.sacct_backfill',
        'gcm.monitoring.cli.sacct_publish',
        'gcm.monitoring.cli.sacct_running',
        'gcm.monitoring.cli.sacct_wrapper',
        'gcm.monitoring.cli.sacctmgr_qos',
        'gcm.monitoring.cli.sacctmgr_user',
        'gcm.monitoring.cli.scontrol',
        'gcm.monitoring.cli.scontrol_config',
        'gcm.monitoring.cli.slurm_job_monitor',
        'gcm.monitoring.cli.slurm_monitor',
        'gcm.monitoring.cli.storage',
        'gcm.monitoring.click',
        'pydantic',
        'pydantic.deprecated',
        'pydantic.deprecated.decorator',
        'pydantic_core',
        'opentelemetry',
        'opentelemetry.sdk',
        'opentelemetry.sdk.trace',
        'opentelemetry.sdk.metrics',
        'opentelemetry.exporter.otlp',
        'opentelemetry.exporter.otlp.proto.grpc',
        'cffi',
        'pynvml',
        'click',
        'omegaconf',
        'tomli',
        'gni',
        'psutil',
        'daemon',
        'clusterscope',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='gcm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='gcm',
)
