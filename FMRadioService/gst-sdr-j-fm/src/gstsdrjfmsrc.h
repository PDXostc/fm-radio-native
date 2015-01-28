/* GStreamer
 * Copyright (C) Collabora Ltd. <info@collabora.com>
 *
 * gstsdrjfmsrc.h:
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 */

#ifndef __GST_SDRJFM_SRC_H__
#define __GST_SDRJFM_SRC_H__


#include <gst/gst.h>
#include <gst/audio/gstaudiosrc.h>

#include <gui.h>

typedef struct _GstSdrjfmSrc GstSdrjfmSrc;
typedef struct _GstSdrjfmSrcClass GstSdrjfmSrcClass;

struct _GstSdrjfmSrc {
  GstAudioSrc    src;

  gint frequency;

  RadioInterface *radio;
};

struct _GstSdrjfmSrcClass {
  GstAudioSrcClass parent_class;

};

extern "C" {

#define GST_TYPE_SDRJFM_SRC           (gst_sdrjfm_src_get_type())
#define GST_SDRJFM_SRC(obj)           (G_TYPE_CHECK_INSTANCE_CAST((obj),GST_TYPE_SDRJFM_SRC,GstSdrjfmSrc))
#define GST_SDRJFM_SRC_CLASS(klass)   (G_TYPE_CHECK_CLASS_CAST((klass),GST_TYPE_SDRJFM_SRC,GstSdrjfmSrcClass))
#define GST_IS_SDRJFM_SRC(obj)        (G_TYPE_CHECK_INSTANCE_TYPE((obj),GST_TYPE_SDRJFM_SRC))
#define GST_IS_SDRJFM_SRC_CLASS(klas) (G_TYPE_CHECK_CLASS_TYPE((klass),GST_TYPE_SDRJFM_SRC))

GType gst_sdrjfm_src_get_type(void);

}

#endif /* __GST_SDRJFM_SRC_H__ */
